# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Dataset
# 2 2 2
# 0.78333

dataset = "16 26 23"
# k = homozygous dominant
k=int(dataset.split(" ")[0])

# m= heterozygous
m=int(dataset.split(" ")[1])

# m= homozygous recessive
n=int(dataset.split(" ")[2])
total = k+m+n

treeK =  ((k/total) * ((k-1)/(total-1)) *1)+ (((k/total) * (n/(total-1))*1))+ ( ((k/total) * (m/(total-1)) *1) ) 
treeM =  ((m/total) * ((m-1)/(total-1)) *0.75)+ (((m/total) * (n/(total-1))*0.5))+ ( ((m/total) * (k/(total-1)) *1) ) 
treeN =  ((n/total) * ((n-1)/(total-1)) *0)+ (((n/total) * (k/(total-1))*1))+ ( ((n/total) * (m/(total-1)) *0.5) ) 

summOfTree = treeK + treeM + treeN

print(summOfTree)
