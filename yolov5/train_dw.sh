# Train YOLOv5s on COCO128 for 3 epochs

# 1 Single-GPU training, use pretrained model
#    epochs建议是300, 600, 1200
#    img 设置640，如果针对小物体的话设置成1280
# python train_dw.py --img 640 --batch 16 --epochs 5 --data ./data/coco128.yaml --weights ./checkpoints/yolov5s.pt



# 2 Single-GPU training, 从头训练，要把weights置空
# python train_dw.py --img 640   --data ./data/coco128.yaml --weights '' --cfg ./models/yolov5s.yaml  # from scratch

#Usage - Multi-GPU DDP training:
#    $ python -m torch.distributed.run --nproc_per_node 2 --master_port 1 train.py --data coco128.yaml --weights yolov5s.pt --img 640 --device 0,1


# 基于yolo5预训练模型来训练bdd100k数据
python train_dw.py --img 640 --batch 32 --epochs 5 --data ./data/bdd_coco.yaml --weights ./checkpoints/yolov5s.pt  --cfg ./models/yolov5s_bdd.yaml --name yolov5s_bdd_prew 
# 从头训练bdd100k数据
# python train_dw.py --img 640 --batch 32 --epochs 5 --data ./data/bdd_coco.yaml --weights ''  --cfg ./models/yolov5s_bdd.yaml  --name yolov5s_bdd
