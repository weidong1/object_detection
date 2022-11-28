# Train YOLOv5s on COCO128 for 3 epochs
python train_dw.py --img 640 --batch 16 --epochs 3 --data ./data/coco128.yaml --weights ./checkpoints/yolov5s.pt