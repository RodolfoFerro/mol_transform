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


def translate(p_mat, vec=None):
    """
    Utility function to translate a set of 3D coordinates
    """
    T = np.eye(4)
    if vec is None:
        T[:-1, 3] = -p_mat[0]
    else:
        T[:-1, 3] = vec
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
args = vars(ap.parse_args())

# Ask for transformation:
print("Okay, we've detected you want to transform {}.".format(args["file"]))

if __name__ == "__main__":
    # Parse args:
    p_mat = read_xyz(args["file"])
    t_vec = args["translate"]
    out_f = args["output"]

    # Traslation:
    t_mat = translate(p_mat, t_vec)

    # Write output:
    write_xyz(out_f, t_mat)
