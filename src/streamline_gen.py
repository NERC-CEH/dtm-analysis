import os
from whitebox import WhiteboxTools
import rasterio
import numpy as np

def generate_streamlines(dem_path, output_dir, flow_accum_threshold=1000):
    """
    Generate streamlines from a DEM using WhiteboxTools.
    
    Parameters:
    -----------
    dem_path : str
        Path to the input DEM file
    output_dir : str
        Directory to store output files
    flow_accum_threshold : int
        Threshold for flow accumulation to define streams (default: 1000)
    """
    try:
        # Initialize WhiteboxTools
        wbt = WhiteboxTools()
        wbt.set_verbose_mode(True)
        wbt.set_working_dir(output_dir)

        # Print WhiteboxTools version for debugging
        print(f"WhiteboxTools version: {wbt.version()}")

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define output file paths
        filled_dem = os.path.join(output_dir, "filled_dem.tif")
        flow_dir = os.path.join(output_dir, "flow_direction.tif")
        flow_accum = os.path.join(output_dir, "flow_accumulation.tif")
        streams = os.path.join(output_dir, "stream_network.tif")
        streamlines = os.path.join(output_dir, "streamlines.shp")

        # Check if input DEM exists
        if not os.path.exists(dem_path):
            raise FileNotFoundError(f"Input DEM file not found: {dem_path}")

        print("Step 1: Filling depressions in DEM...")
        wbt.fill_depressions(
            dem=dem_path,
            output=filled_dem
        )

        print("Step 2: Calculating flow direction...")
        wbt.d8_pointer(
            dem=filled_dem,
            output=flow_dir
        )

        print("Step 3: Calculating flow accumulation...")
        # Using the correct parameters based on the tool parameters output
        wbt.d8_flow_accumulation(
            i=flow_dir,           # Input is the flow direction raster
            output=flow_accum,    # Output file
            out_type="cells",     # Output type
            pntr=True,            # Indicate that input is a pointer
            esri_pntr=False       # Specify pointer style
        )

        print("Step 4: Extracting stream network...")
        wbt.extract_streams(
            flow_accum=flow_accum,
            output=streams,
            threshold=flow_accum_threshold
        )

        print("Step 5: Converting streams to vector streamlines...")
        wbt.raster_streams_to_vector(
            streams=streams,
            d8_pntr=flow_dir,
            output=streamlines,
            esri_pntr=False
        )

        print(f"Streamline generation completed successfully! Output saved to: {streamlines}")

        # Calculate some basic statistics for the stream network
        try:
            with rasterio.open(streams) as src:
                data = src.read(1)
                stream_cells = np.sum(data > 0)
                total_cells = data.size
                stream_percentage = (stream_cells / total_cells) * 100

            print("Stream network statistics:")
            print(f"Total cells: {total_cells}")
            print(f"Stream cells: {stream_cells}")
            print(f"Percentage of stream cells: {stream_percentage:.2f}%")
        except Exception as stats_error:
            print(f"Could not calculate statistics: {str(stats_error)}")

        return streamlines

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    # Example usage
    dem_path = os.path.join(os.getcwd(), "data/raw/54080_dtm.tif")  # Replace with your DEM path
    output_dir = os.path.join(os.getcwd(), "data/interim")  # Replace with your output directory
    flow_accum_threshold = 1000  # Adjust based on your needs

    # Generate streamlines
    result = generate_streamlines(dem_path, output_dir, flow_accum_threshold)

    if result:
        print("Workflow completed successfully!")
    else:
        print("Workflow failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
