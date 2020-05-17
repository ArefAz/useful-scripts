import tensorflow as tf

""" Splits a tfrecord files into multiple shards """

def split_tfrecord(tfrecord_path, split_size): 
   with tf.Graph().as_default(), tf.Session() as sess: 
      ds = tf.data.TFRecordDataset(tfrecord_path).batch(split_size) 
      batch = ds.make_one_shot_iterator().get_next() 
      part_num = 0 
      while True: 
         try: 
            records = sess.run(batch) 
            part_path = tfrecord_path + '.{:03d}'.format(part_num) 
            with tf.python_io.TFRecordWriter(part_path) as writer: 
               for record in records: 
                  writer.write(record) 
                  part_num += 1 
         except tf.errors.OutOfRangeError: break

def main():
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('--num-frames', '-n', help='number of frames in each record file', type=int, default=100)
   args = parser.parse_args()
   num_frames = args.num_frames
   split_tfrecord('train.record', num_frames)

if __name__ == '__main__':
   main()
                                                                                                                                                                                                


