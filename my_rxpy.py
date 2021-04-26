# consume an API end-point using RxPY
import requests # pip install requests
import rx # pip install rx
import json
from rx import operators as ops

# access this API end-point: https://jsonplaceholder.typicode.com/users
def filternames(x, l):
    if(x['name'].startswith(l)): # later make use of the chosen letter
        return x['name']
    else:
        return ''

def main():
    # ask the user which letter they want
    letter = input('Which letter? ')
    content = requests.get('https://jsonplaceholder.typicode.com/users')
    y = json.loads(content.text)
    # use rx to make this an observable
    source = rx.from_(y)
    # use our observable
    case1 = source.pipe(
        ops.filter(lambda c: filternames(c, letter)), 
        ops.map(lambda a: a['name'])
    )
    # wire up the subscription
    case1.subscribe(
        on_next = lambda i: print('Received {}'.format(i)),
        on_error = lambda e: print('Reeceived Error: {}'.format(e)),
        on_completed = lambda: print('All done')
    )

if __name__ == '__main__':
    main()