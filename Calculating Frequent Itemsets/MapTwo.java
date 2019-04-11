import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class MapTwo extends Mapper<IntWritable, Text, Text, LongWritable>
{

    private Text item = new Text();
    private LongWritable one = new LongWritable(1);

    public void map(IntWritable key, Text value, Context context) throws IOException, InterruptedException
    {

        Transactions trans = Helpers.getTrans((int) key.get(), value.toString());

        for (Integer tran : trans)
        {
            String ind = String.valueOf(tran);
            item.set(ind);
            context.write(item, one);
        }

    }

    @Override
    public void setup(Context context) throws IOException
    {

        Configuration config = context.getConfiguration();
        String lastOutput = "SON/notFinal/part-r-00000";

        Path path = new Path(lastOutput);
        FileSystem fs = FileSystem.get(config);

        BufferedReader fils = new BufferedReader(new InputStreamReader(fs.open(path)));

        ArrayList<String> strings = new ArrayList<String>();
        strings.addAll(Arrays.asList(fils.toString().split("\\s+")));

    }

}





