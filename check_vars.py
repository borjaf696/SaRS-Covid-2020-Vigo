import pandas as pd
import sys, os

def check_dfs(df1, df2, column = 'POS'):
	col_2 = 'ALT_DP'
	data_check = df1[column]
	results = {'pos':[],'depth':[],'hit':[]}
	for i,t in enumerate(data_check):
		if t in list(df2[column]):
			results['pos'].append(t)
			results['depth'].append(df1.iloc[i][col_2])
			results['hit'].append(True)
		else:
			results['pos'].append(t)
			results['depth'].append(df1.iloc[i][col_2])
			results['hit'].append(False)
	return pd.DataFrame(results)

def filter_pval(df1, col = 'PVAL'):
	return df1.loc[df1[col] <= 0.05]

if __name__ == '__main__':
	print('python check_vars.py file_ivar file_contigs folder')
	assert len(sys.argv) == 4

	file_ivar, file_contigs = sys.argv[1], sys.argv[2]
	folder = sys.argv[3]
	print('Comparing variants from: ',file_ivar,' & ',file_contigs)
	df_ivar, df_contigs = pd.read_csv(file_ivar, sep='\t'), pd.read_csv(file_contigs,sep='\t')
	df_ivar = filter_pval(df_ivar)
	print(df_ivar)
	df_ivar.to_csv(folder+'/filtered.tsv', sep = '\t')
	check_dfs(df_ivar, df_contigs).to_csv(folder+'/hits.tsv')
