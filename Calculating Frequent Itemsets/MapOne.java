import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

import static java.lang.Integer.parseInt;

public class MapOne extends Mapper<LongWritable, Text, Text, IntWritable>
{

    private Text item = new Text();
    private IntWritable one = new IntWritable(1);

    public MapOne()
    {
    }

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
    {

        Transactions trans = Helpers.getTrans((int) key.get(), value.toString());
        int support = parseInt(context.getConfiguration().get("minSupp"));
        int correction = parseInt(context.getConfiguration().get("correction"));

        for (Integer tran : trans)
        {
            String ind = String.valueOf(tran);
            item.set(ind);
            context.write(item,one);
        }

    }
}
