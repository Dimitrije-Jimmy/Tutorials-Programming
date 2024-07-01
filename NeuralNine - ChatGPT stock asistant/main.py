# GPT powered financial asistant / stop analasys asistant chatbot

# a web aplication with the stock analasys chatbot asistant
# we ask a question and the asistant helps
# we have access to live data from the yahoofinanca API

# we're going to have yahoo finance API, basic tehnical analasys, Open AI API
# and web application using streamlit
# pip install openai pandas matplotlib yfinance streamlit

# in the 'API_KEY' file you put OpenAI api key, you of coure need credits.
# 5 cents per session

import json
import openai
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf
import os


script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# here I'd need to be more specific with directory
openai.api_key = open(script_directory+'\\'+'API_KEY', 'r').read()


# we let ChatGPT call the functions and trust that it knows what the ticker symbol is for a company
# if the ticker changes ChatGPT wouldn't know, you'd have to tell it in description

# all the functions need to return strings because ChatGPT answers with text

# stock price getting
def get_stock_price(ticker):
    # yf.Ticker(ticker) - yahoo finance Ticker
    # .history(period='1y') - 
    # .iloc[-1] - the most current position
    # .Close - closing price
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)


# Simple Moving Average
def calculate_SMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    # .rolling - rolling average in window - timefrace
    # .mean - vzamemo mean
    # .iloc - most current position
    return str(data.rolling(window=window).mean().iloc[-1])


# Exponential Moving Average
def calculate_EMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    # ewm - same thing as before just exponential moving average
    # adjust=False
    return str(data.ewm(window=window, adjust=False).mean().iloc[-1])


# if you want to plot the SMA or EMA just define the function and ChatGPT can utilize it

# Relative Strength Index
def calculate_RSI(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    delta = data.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=14-1, adjust=False).mean()
    ema_down = down.ewm(com=14-1, adjust=False).mean()
    rs = ema_up/ema_down  # relative strength
    return str(100 - (100 / (1+rs)).iloc[-1])


# Moving Average Convergence Divergence
def calculate_MACD(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    short_EMA = data.ewm(span=12, adjust=False).mean()
    long_EMA = data.ewm(span=26, adjust=False).mean()

    MACD = short_EMA - long_EMA
    signal = MACD.ewm(span=9, adjust=False)
    MACD_histogram = MACD - signal

    # have to separate values so that ChatGPT knows what's what
    return f'{MACD[-1]}, {signal[-1]}, {MACD_histogram[-1]}'

# you don't need to implement these indicators yourself
#  you can also use a tehnical analasys library


def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y') # no .Close, we want the whole data
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.Close)
    plt.title(f'{ticker} Stock Price Over Last Year')
    plt.xlabel('Date')
    plt.ylabel('Stock price [$]')
    plt.grid(True)
    plt.savefig('stock.png')
    plt.close()



# to let GPT use these functions we need to define them in a list which contains dictionaries,...
#  basically a JSON file

# the description tells ChatGPT what the function does, it doesn't read the code

functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    }
]

functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    }
]


functions = [
    # function 1 ________________
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    },
    # function 2 ________________
    {
        'name': 'calculate_SMA',
        'description': 'Calculate the simple moving average for a given stock ticker and a windw.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    # function 3 ________________
    {
        'name': 'calculate_EMA',
        'description': 'Calculate the exponential moving average for a given stock ticker and a windw.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the EMA'
                }
            },
            'required': ['ticker', 'window']
        }
    },
    # function 4 ________________
    {
        'name': 'calcualte_RSI',
        'description': 'Calculate the relative strength index for a given stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    },
    # function 5 ________________
    {
        'name': 'calculate_MACD',
        'description': 'Calculate the MACD for a given stock ticker and a short and long window',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    },
    # function 6 ________________
    {
        'name': 'plot_stock_pric',
        'description': 'Plot the stock price for the last year given the ticker symbol of a company',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple). Note: FB is renamed to Meta'
                }
            },
            'required': ['ticker']
        }
    },
]


# we create a dict where we map the functions to their names
available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'calculate_RSI': calculate_RSI,
    'calculate_MACD': calculate_MACD,
    'plot_stock_price': plot_stock_price
}


# we now build the streamlit webapp and we keep track of the messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = [] # we create empty list

st.title('Stock Analysis Chatbot Assistant')

user_input = st.text_input('Your input:')

if user_input:
    try:
        st.session_state['messages'].append({'role': 'user', 'content': f'{user_input}'})
        # ChatGPT has roles: user - us, asistant - GPT, system - contextual information

        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo-0613',
            messages = st.session_state['message'],
            functions = functions,
            function_call = 'auto'
        )

        response_message = response['choices'][0]['message']
        
        if response_message.get('function_call'):
            function_name = response_message['function_call']['name']
            function_args = json.loads(response_message['function_call']['arguments'])
            if function_name in ['get_stock_price', 'calculate_RSI', 'calculate_MACD', 'plot_stock_price']:
                args_dict = {'ticker': function_args.get('ticker')}
            elif function_name in ['calculate_SMA', 'calculate_EMA']: # all other functions take the ticker and window as parameters
                args_dict = {'ticker': function_args.get('ticker'), 'window': function_args.get('window')}

            function_to_call = available_functions[function_name]
            function_response = function_to_call(**args_dict)

            if function_name == 'plot_stock_price':
                st.image('stock.png')
            else:
                st.session_state['messages'].append(response_message)
                st.session_state['messages'].append(
                    {
                        'role': 'function',
                        'name': function_name, 
                        'content': function_response
                    }
                )
                second_response = openai.ChatCompletion.create(
                    model = 'gpt-3.5-turbo-0613',
                    messages = st.session_state['messages']
                )
                st.text(second_response['choices'][0]['message']['content'])
                st.session_state['messages'].append({'role': 'asistant', 'content': second_response['choices'][0]['message']['content']})
        else: # no function call
            st.text(response_message['content'])
            st.session_state['messages'].append({'role': 'assistant', 'content': response_message['content']})
    except Exception as e:
        raise e

# to run this script with streamlit webapp you need to write in CMD
# streamlit run d:/Programming/Tutorials/NeuralNine - ChatGPT stock asistant/main.py [ARGUMENTS]
# streamlit run main.py

# the code currently isn't working but that's because I have no API_KEY for OpenAPI
# but essentially it works, I'm just typing another line to make it 320 