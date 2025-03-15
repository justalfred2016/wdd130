import math

# Store the data as a list of dictionaries
cans_data = [
    {"Name": "#1 Picnic", "Radius (cm)": 6.83, "Height (cm)": 10.16},
    {"Name": "#1 Tall", "Radius (cm)": 7.78, "Height (cm)": 11.91},
    {"Name": "#2", "Radius (cm)": 8.73, "Height (cm)": 11.59},
    {"Name": "#2.5", "Radius (cm)": 10.32, "Height (cm)": 11.91},
    {"Name": "#3 Cylinder", "Radius (cm)": 10.79, "Height (cm)": 17.78},
    {"Name": "#5", "Radius (cm)": 13.02, "Height (cm)": 14.29},
    {"Name": "#6Z", "Radius (cm)": 5.40, "Height (cm)": 8.89},
    {"Name": "#8Z short", "Radius (cm)": 6.83, "Height (cm)": 7.62},
    {"Name": "#10", "Radius (cm)": 15.72, "Height (cm)": 17.78},
    {"Name": "#211", "Radius (cm)": 6.83, "Height (cm)": 12.38},
    {"Name": "#300", "Radius (cm)": 7.62, "Height (cm)": 11.27},
    {"Name": "#303", "Radius (cm)": 8.10, "Height (cm)": 11.11},
]

def cylinder_volume(radius, height):
    #Calculate the volume of a cylinder.
    return math.pi * (radius ** 2) * height

def cylinder_surface_area(radius, height):
    #Calculate the surface area of a cylinder.
    return 2 * math.pi * radius * (radius + height)

def storage_efficiency(volume, surface_area):
    #Calculate storage efficiency (volume / surface area).
    return volume / surface_area

def main():
    # Iterate over the data and calculate metrics for each can
    for can in cans_data:
        name = can["Name"]
        radius = can["Radius (cm)"]
        height = can["Height (cm)"]

        # Calculate volume and surface area
        volume = cylinder_volume(radius, height)
        surface_area = cylinder_surface_area(radius, height)

        # Calculate storage efficiency
        efficiency = storage_efficiency(volume, surface_area)

        # Print results
        print(f"Can: {name}")
        print(f"Radius: {radius} cm, Height: {height} cm")

        print(f"Storage Efficiency: {efficiency:.2f}")
        print("-" * 30)

# Call the main function to execute the program
main()