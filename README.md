# useful-scripts
I add some small python scripts here which could be handy sometimes. 

I did not wrote all of them and some are collected from stackoverflow and github and
tensorflow object_detection api documentation with minor changes.

These scripts are tested on Ubuntu 18.04 LTS and might not work on other OSs other than linux without editing os.system() commands.

**Usage:**

1. `python clear_dataset.py /path/to/dataset/directory`

2. `python move_xmls /path/to/image+xmls/directory`

3. `python save_frames /path/to/video --name an_arbitrary_name`

4. `python split_rfrecord.py --num-frames 100`

5. from tensorflow object_detection directory: `python xml_to_csv`
Note that your data should have this structure: 
    
        images
            test
            train
            
6. `partition_dataset.py -i IMAGEDIR -r RATIO -x` 

##### please open an issue if you find a bug

