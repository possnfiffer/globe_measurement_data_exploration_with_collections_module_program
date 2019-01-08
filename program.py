from collections import defaultdict, namedtuple, Counter
import csv


MEASUREMENT_CSV = "GLOBEMeasurementData.csv"


Measurement = namedtuple(
    "Measurement", "site org latitude longitude elevation measured_on current_temp"
)


def get_measurements_by_site(data=MEASUREMENT_CSV):
    """Extracts all measurements from csv and stores them in a dictionary
       where keys are sites, and values is a list of measurements"""
    measurements = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                site = line[" site_name"]
                org = line["org_name"]
                latitude = line[" latitude"]
                longitude = line[" longitude"]
                elevation = line[" elevation"]
                measured_on = line[" measured_on"]
                current_temp = line["air temps:current temp (deg C)"]
            except ValueError:
                continue

            m = Measurement(
                site=site,
                org=org,
                latitude=latitude,
                longitude=longitude,
                elevation=elevation,
                measured_on=measured_on,
                current_temp=current_temp,
            )
            measurements[site].append(m)

    return measurements


def main():

    measurements = get_measurements_by_site()

    cnt = Counter()
    for site, current_temp in measurements.items():
        cnt[site] += len(current_temp)

    print("The five sites with the most air temp measurements are...")
    print(cnt.most_common(5))


if __name__ == "__main__":
    main()
