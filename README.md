## Introduction
This repository is created for purposes of Data Science career path at codecademy to showcase Seaborn/matplotlib skills. This is an updated version of first README file, since I felt that I left this code without any explanation nor analysis. This will also be (probably!) the final version of analysis, because I found provided data not meaningful and I honestly think that creating various versions of the same distribution just to prove a point that I can do that is a waste of time. Secondly, I find this data really boring, I'd rather work on economic or technical data 😂.

I'd like to begin with some basic info about data and analysis. Firstly, my task was to play around datasets provided by codecademy containing artificial data about biodiversity in US national parks. The idea was to showcase my pandas, Seaborn and matplotlib skills. I won't be discussing code here, because after running it, you'll get the same graphs as will be placed below. You can find packages necessary to run the code in setup.py file.

To see graphs, run `main.py`. Please note, that in order to run it, you must have *observations.csv* and *species_info.csv* files in the same directory as `main.py`. 

## Analysis
I had to merge two datasets into one, *merged.csv*, so that I could work on data more smoothly. If you wish to generate *merged.csv*, just uncomment the last line of code in the `#importing data, merging into one csv` section. Without further ado, let's dive into first graph:

### Observations 
<p align="center">
  <img width="1079" alt="Zrzut ekranu 2022-06-14 o 22 15 19" src="https://user-images.githubusercontent.com/80947256/173680605-58b81450-af1f-44b9-99ea-9f222c4b48f1.png">
</p>

As you can see, the most observations were made in Yellowstone National Park and the least in Great Smoky Mountains Park. Let's look at the categorical distribution of observations by park:

### Distributions
<p align="center">
  <img width="1065" alt="Zrzut ekranu 2022-06-14 o 22 23 22" src="https://user-images.githubusercontent.com/80947256/173681811-a859eff1-df84-426e-848d-ec27e3fc574a.png">
</p>
Now, just a second! This is a boxplot of observations of each category and every point in this data set were observations of certain species. For an example:


- Park name: Yellowstone National Park
- Category: Mammal
- Species: Canis lupus
- Observations: 235

What's interesting about this boxplot is how median observation in each of the category in every park and total observations by category in every is nearly identical. Certainly, in nearly every category there are some outliers. Ones that are closer to zero may be good suspects of endangered species. Speaking of, let's see endangerment of speices by categories:

### Endangerment
<p align="center">  
  <img width="1069" alt="Zrzut ekranu 2022-06-14 o 22 46 36" src="https://user-images.githubusercontent.com/80947256/173685854-37f110fd-ae77-4683-a3a7-6438ce8e8726.png">
</p>

Here are categories by total endangered species... Yeah it doesn't look too good. So take a look at conservation statuses in percents:


![Zrzut ekranu 2022-06-14 o 22 46 24](https://user-images.githubusercontent.com/80947256/173686196-30931e1a-d503-4588-a2ac-b41a473d75db.png)

Much better. Apparently, most endangered categories are: Mammals and Bird, although some small bit of Birds seem to start recovering.

## To sum up...
During creating this README I noticed that I could work more on three problems:

- finding out which specifi species are endangered (with help of boxplot),
- finding out why there is a huge difference in total observations in parks (I suspect that some of the data was engineered by looking at Yellowstone vs. Yosemite),
- most frequently spotted animal.

The key take-away is probably that plants in US aren't endangered and we should look after mammals and birds more. It wasn't fun. It was pain. I'll try to update it in my freetime. Thank for getting through this analysis and see you soon. 
