# Train YOLOv5s on COCO128 for 3 epochs

# 1 Single-GPU training, use pretrained model
python train_dw.py --img 640 --batch 16 --epochs 5 --data ./data/coco128.yaml --weights ./checkpoints/yolov5s.pt


# 2 Single-GPU training, 从头训练
# python train_dw.py --img 640   --data ./data/coco128.yaml --weights '' --cfg yolov5s.yaml  # from scratch

#Usage - Multi-GPU DDP training:
#    $ python -m torch.distributed.run --nproc_per_node 4 --master_port 1 train.py --data coco128.yaml --weights yolov5s.pt --img 640 --device 0,1,2,3
