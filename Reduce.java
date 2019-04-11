import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

import static java.lang.Integer.parseInt;

public class Reduce extends Reducer<Text, IntWritable, Text, IntWritable>
{

    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException
    {
        int minsup = parseInt(context.getConfiguration().get("minSupp"));
        int correction = parseInt(context.getConfiguration().get("correction"));
        int count = 0;

        for (IntWritable value : values)
            count += value.get();
        if (count >= minsup - correction)
            context.write(key, new IntWritable(count));
    }
}
