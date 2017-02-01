#Translates a protein sequence back into DNA sequence

from Bio.Alphabet import IUPAC

from Bio.Seq import Seq

#import string
import random

protein_seq=Seq("MRHTWLFVTACAMALSSTAQAQDAKALEQLEVISRSYAKDNHVAEAEASRRLELRQVL\
ARPEIEAFKADYADRLDTAYWDDSRDGFKLVLRLKQGPLPAIHELSTTHGTIPVKFTLVS", IUPAC.protein)

print protein_seq

print " "
convert_to_dna_str=str(protein_seq)

dna=""



#dict is a dictionary that help map the keys such a "M" to values suchs as "ATG"

dict={"M":["ATG"],"R":["CGT", "CGC", "CGA", "CGG","AGA", "AGG"],\
      
      "H":["CAT", "CAC"], "T": ["ACT", "ACC", "ACA", "ACG"],\

      "W":["TGG"], "L":["TTG","TTA", "CTT", "CTC", "CTA", "CTG"],\

      "F":["TTT", "TTC"],"V":["GTT","GTC","GTA", "GTG"],\

      "A":["GCT", "GCC", "GCA", "GCG"],"S":["TCT", "TCC","TCA","TCG","AGT","AGC"],\

      "Q":["CAA","CAG"],"D":["GAT", "GAC"], "K":["AAA","AAG"], "E":["GAA","GAG"],\

      "I":["ATT", "ATC","ATA"],"Y":["TAT", "TAC"], "N":["AAT","AAC"],\

      "P":["CCT", "CCC", "CCA", "CCG"], "G":["GGT", "GGC","GGA","GGG"]

     }



#loops through the protein sequence
for i in convert_to_dna_str:
   
   #loops through the key,s such as "H", in the dictionary 
   for key in dict.keys():
       if i==key:
          x=random.choice(dict[key])
          
          #print x
          dna+=x
   
       


print dna    


print " "
