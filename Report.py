import matplotlib.pyplot as plt
import numpy as np
class Report:
    def generateReport(self, sqlscore, xssscore, nmapscore, dupscore):
        label = ['SQL Injection', 'XSS', 'Nmap', 'Default Username and Password']
        no_movies = [sqlscore, xssscore, nmapscore, dupscore]
        # this is for plotting purpose
        index = np.arange(len(label))
        plt.bar(index, no_movies)
        plt.xlabel('Attacks', fontsize=15)
        plt.ylabel('Score', fontsize=15)
        plt.xticks(index, label, fontsize=15, rotation=30)
        plt.title('Website Analysis')
        plt.show()

	
