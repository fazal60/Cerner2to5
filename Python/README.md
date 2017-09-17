# Cerner2^5

## The script
* This folder in the repo contains a Python script named *Cerner2to5.py*
* This script uses Walmart API to find out whether the item your are searching in the store of your choice.
* The information is returned in JSON format.

## Installation and Usage
* [API Documentation](https://developer.walmartlabs.com/docs)
* I have hardcoded my own API_Key for the purpose of this demo.
* You need to pass in Zipcode and item name to find if the item is present in the walmart closest to the zipcode provided.

```
git clone https://github.com/sheikhms60/Cerner2to5.git
cd Cerner2to5
cd Python
python Cerner2to5 66223 Cheese
```
### Expected result
```
Closest walmart is:Overland Park Walmart Supercenter, 15700 Metcalf Ave, Overland Park, KS
Cheese Found at Overland Park Walmart Supercenter
```

### Edge cases
* If you don't pass any argument, zipcode defaults to your current location zipcode and item defaults to Milk.
* If you pass in just 1 argument, its construed as a Zipcode. If its invalid, zipcode defaults to your current location zipcode and item defaults to Milk.
* If you pass in a stopword for itemname, i.e., second argument, item defaults to Milk.




