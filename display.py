from IPython.display import display
import pandas

dic = {
    'nome' : 'gabriel',
     'idade' : '21'
}

df = pandas.DataFrame(dic)
 
# displaying the DataFrame
display(df)