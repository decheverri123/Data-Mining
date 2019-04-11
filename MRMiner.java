import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import java.io.IOException;

import static java.lang.System.err;

public class MRMiner extends Configured implements Tool
{

    static boolean setUp(String input, String notFinalOutput, String output, int passes, int minSupp, Integer transPer,
                         int correction) throws IOException, ClassNotFoundException, InterruptedException
    {

        Configuration conf = new Configuration();

        conf.setInt("minSupp", minSupp);
        conf.setInt("passes", passes);
        conf.setInt("transPer", transPer);
        conf.setInt("correction", correction);

        Job job = Job.getInstance(conf, String.format("MRMiner%d", passes));
        job.setJarByClass(MRMiner.class);

        if (passes == 1)
        {
            FileInputFormat.addInputPath(job, new Path(input));
            FileOutputFormat.setOutputPath(job, new Path(notFinalOutput));
            job.setMapperClass(MapOne.class);
        }

        else
        {
            FileInputFormat.addInputPath(job, new Path(String.format("./%s/part-r-00000", notFinalOutput)));
            FileOutputFormat.setOutputPath(job, new Path(output));
            job.setMapperClass(MapTwo.class);

        }

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        job.setReducerClass(Reduce.class);
        return (job.waitForCompletion(true));
    }

    public static void main(String[] args) throws Exception
    {
        int exitCode = ToolRunner.run(new MRMiner(), args);
        System.exit(exitCode);
    }

    public int run(String[] args) throws Exception
    {
        if (args.length != 6)
            err.println(
                    "USAGE:  hadoop jar mr.jar MRMiner MINSUPP CORR TRANS_PER_BLOCK PATH_TO_INPUT PATH_TO_FIRST_OUT PATH_TO_FINAL_OUT");

        int minSupp = Integer.parseInt(args[0]);
        int correction = Integer.parseInt(args[1]);
        int transPer = Integer.parseInt(args[2]);
        String input = args[3];
        String firstOut = args[4];
        String finalOut = args[5];

        for (int i = 1; i <= 2; i++)
        {
            boolean b = setUp(input, firstOut, finalOut, i, minSupp, transPer, correction);
            if (!b)
            {
                err.println("Oof");
                return -1;
            }
        }

        return 1;
    }

}
