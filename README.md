# yolov7

Implementation of "YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors"

This implementation is based on [yolov7](https://github.com/WongKinYiu/yolov7).

# How to run

Store your image sequence inside  `seg/data/images` directory, also store the ground truth masks inside `seg/data/gt` directory. Images and masks are sorted by filenames, so keep the filename numerical (Ideally 5 digit starting with `00000.(jpg|png)`)

Then go inside `seg/` and run the following:

```
python segment/predict.py 
```

The output will be stored in `runs/` directory.

# Running in docker

you can run a docker container with the following command:

```
docker build -t yolov7 . && \
docker run -v host_images_dir:/app/seg/data/images -v host_ground_truth_dir:/app/seg/data/gt -v host_output_dir:/app/seg/runs  yolov7
```

For example, this exact command in local machine is run to generate the outputs.

```
docker build -t yolov7 . && \
docker run -v C:\Users\ge79pih\tmo_data\tmo\tmo_dataset\street:/app/seg/data/images -v C:\Users\ge79pih\tmo_data\tmo\tmo_gt\street:/app/seg/data/gt -v C:\Users\ge79pih\tmo_data\tmo\tmo_output:/app/seg/runs  yolov7
```
