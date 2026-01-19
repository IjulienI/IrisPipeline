import pymel.core as pm
import random as rand

# clouds settings
box_height = 10
box_lenghtX = 10
box_lenghtY = 20

ball_count = 100
ball_min_radius = 0.3
ball_max_radius = 2

# save path
save_path = "C:/Users/julien.soum/Documents/maya/projects/Cloud_Test.mb"

# delete root
if pm.objExists("root"):
    pm.delete(root)

# create root
root = pm.createNode("transform", name="root")
mesh = pm.createNode("transform", name="mesh")
pm.parent(mesh, root)

# generate cloud
for i in range(ball_count):
    transform, node = pm.polySphere(r=rand.uniform(ball_min_radius, ball_max_radius))
    transform.translate.set(rand.uniform(0, box_lenghtX), rand.uniform(0, box_height), rand.uniform(0, box_lenghtY))
    pm.parent(transform, mesh)

# save the current scene
pm.saveAs(save_path, f=True)