import xarray as xr
from pathlib import Path

# MET required attributes
required_attributes = {
    "id": "Required if not hosted by MET",
    "naming_authority": "Required if not hosted by MET",
    "title": "Required",
    "summary": "Required",
    "keywords": "Required, GCMD Science Keywords",
    "keywords_vocabulary": "Required, GCMD Science Keywords",
    "geospatial_lat_min": "Required",
    "geospatial_lat_max": "Required",
    "geospatial_lon_min": "Required",
    "geospatial_lon_max": "Required",
    "time_coverage_start": "Required",
    "time_coverage_end": "Required",
    "Conventions": "Required",
    "history": "Required",
    "date_created": "Required",
    "creator_type": "Required",
    "creator_institution": "Required",
    "creator_name": "Required",
    "creator_email": "Required",
    "creator_url": "Required",
    "publisher_name": "Required if not hosted by MET",
    "publisher_email": "Required if not hosted by MET",
    "publisher_url": "Required if not hosted by MET",
    "project": "Required",
    "license": "Required"
}


def check_compliance(file_path):
    file_path = Path(file_path)
    # Open NetCDF
    with xr.open_dataset(file_path) as ds:
        # Get the global attributes
        global_attrs = ds.attrs

        # Initialize lists to store missing and empty attributes
        missing_attributes = []
        empty_attributes = []

        # Check each required attribute
        for attr, description in required_attributes.items():
            if attr not in global_attrs:
                missing_attributes.append(attr)
            elif global_attrs[attr] is None or global_attrs[attr] == '':
                empty_attributes.append(attr)

        # Print the results
        if missing_attributes or empty_attributes:
            print("\nFile metadata is missing or has empty the following required global attributes:")
            print("===============================================================================")
            for attr in missing_attributes:
                print(f"  - {attr}: {required_attributes[attr]}   (MISSING)")
            for attr in empty_attributes:
                print(f"  - {attr}: {required_attributes[attr]} (EMPTY)")
            print("\nSummary:\n========")
            if len(missing_attributes) > 0:
                print(f"- {len(missing_attributes)} required global attributes are missing.")
            if len(empty_attributes) > 0:
                print(f"- {len(empty_attributes)} required global attributes are empty.")
            print("- Please refer to the ADC compliance documentation to resolve these issues:")
            print("  \033[4m\033[34mhttps://adc.met.no/node/4\033[0m")
            print("\nResult:\n=======")
            result = f"❌ {file_path.name} metadata\x1b[1;31m is not ADC compliant!\033[0m"
        else:
            print("\nSummary:\n========")
            print("- File metadata has all required attributes and they are non-empty.")
            print("\nResult:\n=======")
            result = f"✅ {file_path.name} metadata\x1b[1;32m is ADC compliant!\033[0m"
    return result
