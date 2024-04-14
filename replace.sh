#!/usr/bin/bash

# Find the location of the CSV file
csv_location=$(find . -name 'driving_log.csv')
folder_location=$(dirname "$csv_location")

echo "New name:"
read new_name

# Extract the first column from the CSV file and remove any carriage returns
awk -F',' '{print $1}' "$csv_location" | tr -d '\r' | awk -F'/' '{print $4"/"$5}' > center
awk -F',' '{print $2}' "$csv_location" | tr -d '\r' | awk -F'/' '{print $4"/"$5}' > left
awk -F',' '{print $3}' "$csv_location" | tr -d '\r' | awk -F'/' '{print $4"/"$5}' > right

file_extension='.jpg'

mkdir -p $folder_location/data

i=0
# Loop through each entry in the center file
while IFS= read -r entry; do
  # Construct the source and destination file paths
  source_file="${folder_location}/${entry}"
  destination_file="${folder_location}/data/${new_name}_center_${i}${file_extension}"

  # Move the file to the destination
  cp -r "$source_file" "$destination_file"
  
  ((i++))
done < center

echo "DONE"
