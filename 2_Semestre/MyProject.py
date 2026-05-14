import math

def distance3D(x1, y1, z1, x2, y2, z2):

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    
    return math.sqrt(dx**2 + dy**2 + dz**2)


def circuit3D(x_list, y_list, z_list):

    if not (isinstance(x_list, list) and isinstance(y_list, list) and isinstance(z_list, list)):
        print("************ ERROR ************")
        print("The arguments for circuit3D() should be lists.")
        print("*******************************")
        return None

    if not (len(x_list) == len(y_list) == len(z_list)):
        print("************ ERROR ************")
        print("The lists should have the same length.")
        print("*******************************")
        return None

    n = len(x_list)

    if n == 0 or n == 1:
        print("************ ERROR ************")
        print("The lists should have at least 2 elements.")
        print("*******************************")
        return 0.0

    for i in range(n):
        if not isinstance(x_list[i], (int, float)) \
        or not isinstance(y_list[i], (int, float)) \
        or not isinstance(z_list[i], (int, float)):
            print("************ ERROR ************")
            print("The elements inside the lists should be numbers.")
            print("*******************************")
            return None

    totalDistance = 0.0

    for i in range(n - 1):
        totalDistance += distance3D(
            x_list[i], y_list[i], z_list[i],
            x_list[i+1], y_list[i+1], z_list[i+1]
        )

    totalDistance += distance3D(
        x_list[-1], y_list[-1], z_list[-1],
        x_list[0], y_list[0], z_list[0]
    )

    return totalDistance

def testImplementation():
    
    print("####### TESTS #######")
    
    # -------------------------
    
    x_list = [0, 1, 0]
    y_list = [0, 0, 1]
    z_list = [0, 0, 0]
    
    print("The distance is:", circuit3D(x_list, y_list, z_list))
    
    # -------------------------
    
    print("The distance is:", circuit3D([], [], []))
    
    # -------------------------
    
    print("The distance is:", circuit3D([1], [2], [3]))
    
    # -------------------------
    
    print("The distance is:", circuit3D([0,1], [0], [0,1]))
    
    # -------------------------
    
    x_list = [0.0, 1.5, 2.5]
    y_list = [1.0, 2.0, 3.5]
    z_list = [0.5, 1.5, 2.5]
    
    print("The distance is:", circuit3D(x_list, y_list, z_list))
    
    # -------------------------
    
testImplementation()
