# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:02:23 2020
Correlation between Carbon Emissiona and per capita GDP


@author: Ameya Naik
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd 


indicator_df  = pd.read_csv("D:\MOOC_Courses\Youtube_Projects\WorldDevelopmentIndicator\Archive\Indicators.csv");
indicator_df.info();
indicator_df.head();
indicator_df.shape

indicator_df.isnull().any()


countries = indicator_df['CountryName'].unique().tolist();
len(countries)
indicators = indicator_df['IndicatorName'].unique().tolist();
len(indicators);
years = indicator_df['Year'].unique().tolist();
len(years);
print(min(years), '-',max(years));

#GDP per capita (current US$),NY.GDP.PCAP.CD

indicator_df.columns;

indicator_df.set_index('CountryCode',inplace = True, drop = False);

indicator_df.drop(['HIC', 'OEC', 'OED', 'NOC', 'CEB', 'EAP', 'EMU', 'ECS', 'ECA', 'EUU', 'LCN', 'FCS', 'LAC', 'LMY', 'MEA', 'MNA', 'MIC', 'NAC', 'SSF', 'UMC', 'SSA', 'LMC', 'EAS', 'HPC', 'LDC', 'LIC'], axis=0);
indicator_df.reset_index(drop=True)
co2_emission =indicator_df[indicator_df['IndicatorCode'].str.contains('EN.ATM.CO2E.KT')];
print(co2_emission.head());


gdp_percapita =indicator_df[indicator_df['IndicatorCode'].str.contains('NY.GDP.PCAP.CD')];
print(gdp_percapita.head());


# get the years
years = co2_emission['Year'].values
# get the values
co2 = co2_emission['Value'].values

# create
plt.bar(years,co2)
plt.title("CO2 emission from 1960-2014")
plt.xlabel("Year")
plt.ylabel("CO2Emssion per kIlo Tons ")


#get the years
years = gdp_percapita['Year'].values
# get the values
co2 = gdp_percapita['Value'].values

#create
plt.bar(years,co2)
plt.title("GDP per capita")
plt.xlabel("Year")
plt.ylabel("GDP per capita ")


#Filter for Belgium 
co2_emission_BEL = co2_emission[co2_emission['CountryCode'].str.contains('BEL')];
years = co2_emission_BEL['Year'].values
co2_BEL = co2_emission_BEL['Value'].values

#Filter for USA 
co2_emission_USA = co2_emission[co2_emission['CountryCode'].str.contains('USA')];
co2_UAS = co2_emission_USA['Value'].values
years = co2_emission_USA['Year'].values

#Filter for INDIA 
co2_emission_IND = co2_emission[co2_emission['CountryCode'].str.contains('IND')];
years = co2_emission_IND['Year'].values
co2_IND = co2_emission_IND['Value'].values

#Filter for Germany 
co2_emission_DEU = co2_emission[co2_emission['CountryCode'].str.contains('DEU')];
years = co2_emission_DEU['Year'].values
co2_DEU = co2_emission_DEU['Value'].values

plt.plot(years,co2_UAS, label = "USA")

plt.plot(years,co2_DEU, label = "DEU" )
plt.plot(years,co2_IND, label = "India")
plt.xlabel('Years')
plt.ylabel('CO in tonnes')
plt.legend()
plt.show()

co2_emission =indicator_df[indicator_df['IndicatorCode'].str.contains('EN.ATM.CO2E.KT')];
co2_emission.set_index('CountryCode',inplace = True, drop = False);
co2_emission = co2_emission.drop(['WLD','ARB','HIC', 'OEC', 'OED', 'NOC', 'CEB', 'EAP', 'EMU', 'ECS', 'ECA', 'EUU', 'LCN', 'FCS', 'LAC', 'LMY', 'MEA', 'MNA', 'MIC', 'NAC', 'SSF', 'UMC', 'SSA', 'LMC', 'EAS', 'HPC', 'LDC', 'LIC'], axis=0);
co2_emission = co2_emission.reset_index(drop=True)
co2_emission = co2_emission.sort_values('Value',ascending = False)
co2_emission2014 = co2_emission[co2_emission['Year'] == 2011]
print(co2_emission2014.head(10));
co2_emission1960 = co2_emission[co2_emission['Year'] == 1960]
print(co2_emission1960.head(10));

plt.bar(co2_emission2014['CountryName'].head(10),co2_emission2014['Value'].head(10),label = "2011" )
plt.bar(co2_emission1960['CountryName'].head(10),co2_emission1960['Value'].head(10),label = "1960")
plt.title("Top CO2 emittors in 2011 vs 1960 ")
plt.xlabel("Countries")
plt.ylabel("CO2Emssion per kIlo Tons ")
plt.xticks(rotation = 90)
plt.legend()

gdp_percapita =indicator_df[indicator_df['IndicatorCode'].str.contains('NY.GDP.PCAP.CD')];
gdp_percapita.set_index('CountryCode',inplace = True, drop = False);
gdp_percapita = gdp_percapita.drop(['WLD','ARB','HIC', 'OEC', 'OED', 'NOC', 'CEB', 'EAP', 'EMU', 'ECS', 'ECA', 'EUU', 'LCN', 'FCS', 'LAC', 'LMY', 'MEA', 'MNA', 'MIC', 'NAC', 'SSF', 'UMC', 'SSA', 'LMC', 'EAS', 'HPC', 'LDC', 'LIC'], axis=0);
gdp_percapita = gdp_percapita.reset_index(drop=True)
gdp_percapita = gdp_percapita.sort_values('Value',ascending = False)
gdp_percapita2011 = gdp_percapita[gdp_percapita['Year'] == 2011]
print(gdp_percapita2011.head(10));
gdp_percapita1960 = co2_emission[co2_emission['Year'] == 1960]
print(gdp_percapita1960.head(10));

plt.bar(gdp_percapita2011['CountryName'].head(10),co2_emission2014['Value'].head(10),label = "2011" )
plt.bar(gdp_percapita1960['CountryName'].head(10),co2_emission1960['Value'].head(10),label = "1960")
plt.title("Top GDP per capita  2011 vs 1960 ")
plt.xlabel("Countries")
plt.ylabel("GDP per capita ")
plt.xticks(rotation = 90)
plt.legend()
















