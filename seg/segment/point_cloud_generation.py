import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import matplotlib.image as mpimg

# Depth camera parameters:
FX_DEPTH = 411.9532675638686
FY_DEPTH = 396.0686482174296
CX_DEPTH = 323.57535317408457
CY_DEPTH = 243.6098441558203

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    # Showing outliers (red) and inliers (gray)
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    o3d.visualization.draw_geometries([inlier_cloud])

def show_mask(filename, mask):
    depth_image = iio.imread('~/Downloads/000000.png')

    # get one image by averaging four polarization images
    # rgb_image = iio.imread('avg.png')

    # get only the colors of object
    pixel_loc_of_obj_mask = mask.cpu().detach().numpy()

    # pixel_stack = np.stack((pixel_loc_of_obj_mask, pixel_loc_of_obj_mask, pixel_loc_of_obj_mask), axis=-1)
    # object_rgb = rgb_image * pixel_stack
    # get depth map of the object
    object_depth_image = depth_image * pixel_loc_of_obj_mask

    # compute point cloud for the object:
    pcd = []
    height, width = object_depth_image.shape
    for i in range(height):
        for j in range(width):
            z = object_depth_image[i][j]/1000.0
            if z < 0.01: # The min value 0 represents the noise (there is no distance)
                continue
            x = (j - CX_DEPTH) * z / FX_DEPTH
            y = (i - CY_DEPTH) * z / FY_DEPTH
            pcd.append([x, y, z])
        
    pcd = np.array(pcd)

    #outliers removal
    pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)  # set pcd_np as the point cloud points
    #o3d.visualization.draw_geometries([pcd_o3d])

    # o3d.visualization.draw_geometries([pcd_o3d]) # depth-colored pcd
    cl, ind = pcd_o3d.remove_radius_outlier(nb_points=20, radius=0.005)
    cl, ind = pcd_o3d.remove_statistical_outlier(nb_neighbors=40, std_ratio=2.0)
    cl = cl.paint_uniform_color([0.6, 0.6, 0.6])
    r = o3d.io.write_point_cloud(filename, cl)
    print("{} inserted: {}".format(filename, str(r)))
    #o3d.visualization.draw_geometries([cl])
