#! /bin/bash


# Create new directory to save processed files (if the directory already existed, remove and recreat it)
rm -rf bandpass_karnchana && mkdir bandpass_karnchana

 
for filename in bandpass_raw/*; do

    # Create the array of file extensions to count and print out later
    ext_list+=($(echo "$filename" | cut -d '.' -f2))
    
    # Create the array of filenames without extensions, that will be used to rename files
    name=$(echo "$filename" | cut -d '/' -f2 | cut -d '.' -f1)

    # Check files if they have 'photon' or 'energy' and rename them
    if grep -q "photon" "$filename"; then
       cp ./"$filename" ./bandpass_karnchana/"$name".photons.filt
    else
       cp ./"$filename" ./bandpass_karnchana/"$name".energy.filt
    fi

done


# Print the count of each extension
printf "%s\n" "${ext_list[@]}" | sort | uniq -c 


