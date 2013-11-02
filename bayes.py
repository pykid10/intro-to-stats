# Author: Aadi Dass-Vattam (with Swaroop Vattam's help)
# Date: 11/1/2013
# Program to compute posterior probability using Bayes approach.


#p0 = prior = p(c)
#p1 = sensitivity = p(pos|c)
#p2 = specitivity = p(Neg|!c)

p0=0.2
p1=0.9
p2=0.9

def norm(p0,p1,p2):
    # this function computes the normalizer
    norm = (p0*p1)+((1-p0)*(1-p2)) #norm = normalizer
    return norm

def bayes_positive(p0,p1,p2):
    # this function computes posterior given a positive evidence
    num = p0*p1
    denom = norm(p0,p1,p2)
    posterior = num/denom
    return posterior

def bayes_negative(p0,p1,p2):
    # this function computes posterior given a negative evidence
    num = (1-p0)*(1-p2)
    denom = norm(p0,p1,p2)
    posterior = num/denom
    return posterior
    
pGivenPos = bayes_positive(p0,p1,p2)
pGivenNeg = bayes_negative(p0,p1,p2)
print "p given pos = ",pGivenPos
print "p given neg = ",pGivenNeg
print "total p = (p given pos)+(p given neg) = ",pGivenPos+pGivenNeg

    
    
    
