# ADC-compliance-checker
Arctic Data Centre compliance checker is a python based tool for those wanting to submit data to the Artic Data Centre. The python module can be used to check if files fullfill the rquirements listed [here](https://adc.met.no/node/4).

The compliance checker can be used in combination with CF and ACDD chekcers to enusre NetCDF files adhere to the FAIR principles for data management.

## Usage

### Command Line
```sh
adc-compliance-checker <file_path>
```

#### Output

The tool will provide feeback on the compliance status of the file:
```sh
File has all required attributes and they are non-empty.

\033[1;32mfile.nc is ADC compliant!\033[0m
```
or
```sh
File is missing or has empty the following required attributes:
  - id: Required if not hosted by MET (MISSING)
  - naming_authority: Required if not hosted by MET (MISSING)
  - summary: Required (MISSING)
  - ...

\033[1;31mfile.nc is not ADC compliant!\033[0m
```


### As a Python Package