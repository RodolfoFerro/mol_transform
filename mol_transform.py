import argparse
import numpy as np


def read_xyz(filename):
    """
    Utility function to read a xyz file.
    It returns a numpy matrix for a posterior transformation.
    """
    xyz = open(filename, "r")
    n_lns = int(xyz.readline())
    p_mat = np.zeros((20, 3))
    for l in range(n_lns + 1):
        ps = xyz.readline().split(" ")
        if l > 0:
            ps[-1] = ps[-1][:-1]
            ps = list(filter(lambda x: x != "" and x != "\n", ps))
            p_mat[l - 1] = np.array([float(ps[1]), float(ps[2]), float(ps[3])])
    xyz.close()
    return p_mat


def write_xyz(filename, p_mat):
    """
    Utility function to write a xyz file.
    """
    xyz = open(filename, "w")
    xyz.write("{}\n".format(len(p_mat)))
    xyz.write("\n")
    for line in range(len(p_mat)):
        xyz.write("C\t\t {: .5f}\t {: .5f}\t {: .5f}\n".format(
            p_mat[line, 0], p_mat[line, 1], p_mat[line, 2]))
    xyz.close()


def center(p_mat):
    """
    Utility function to center a set of 3D coordinates.
    """
    print("(WARNING) Not single transformation selected.")
    print("(INFO) Molecule centering to be done.")
    min_x, max_x = np.min(p_mat[:, 0]), np.max(p_mat[:, 0])
    min_y, max_y = np.min(p_mat[:, 1]), np.max(p_mat[:, 1])
    min_z, max_z = np.min(p_mat[:, 2]), np.max(p_mat[:, 2])
    mean_x = (max_x + min_x) / 2
    mean_y = (max_y + min_y) / 2
    mean_z = (max_z + min_z) / 2
    t_vec = [-mean_x, -mean_y, -mean_z]
    t_mat = translate(p_mat, t_vec)
    return t_mat


def translate(p_mat, translation_vec=None):
    """
    Utility function to translate a set of 3D coordinates.
    """
    T = np.eye(4)
    T[:-1, 3] = translation_vec
    print("(INFO) Transformation matrix to be used:")
    print(T)
    t_mat = p_mat.copy()
    for row in range(len(p_mat)):
        t_mat[row] = (T @ np.hstack((p_mat[row], [1])))[:-1]
    return t_mat


def scale(p_mat, scaling_vec=None):
    """
    Utility function to rotate a set of 3D coordinates.
    """
    T = np.eye(4)
    if scaling_vec is None:
        return p_mat
    else:
        T[:-1, :-1] *= scaling_vec
        print("(INFO) Transformation matrix to be used:")
        print(T)
    t_mat = p_mat.copy()
    for row in range(len(p_mat)):
        t_mat[row] = (T @ np.hstack((p_mat[row], [1])))[:-1]
    return t_mat


# Construct the argument parser:
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="Path to input .xyz file.")
ap.add_argument("-o", "--output", required=True,
                help="Path to output .xyz file.")
ap.add_argument("-t", "--translate", required=False, nargs='+', type=float,
                help="Translation vector.")
ap.add_argument("-s", "--scale", required=False, nargs='+', type=float,
                help="Scaling vector.")
args = vars(ap.parse_args())


if __name__ == "__main__":
    # Parse args:
    p_mat = read_xyz(args["file"])
    t_vec = args["translate"]
    s_vec = args["scale"]
    out_f = args["output"]

    # Info about input:
    print("(INFO) Input file to be transformed: {}.".format(args["file"]))

    # Transformations:
    if t_vec:
        T_mat = translate(p_mat, t_vec)
    elif s_vec:
        T_mat = scale(p_mat, s_vec)
    else:
        T_mat = center(p_mat)

    # Write output:
    write_xyz(out_f, T_mat)
    print("(INFO) Processing done.")

    # Info about output:
    print("(INFO) The output file was stored in: {}.".format(args["output"]))
