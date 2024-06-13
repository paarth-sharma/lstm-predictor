# LSTM-PREDICTOR
### small-scale prototyping of a lstm analysis of NSE stocks and their OHLC data

#### Features
- [x] Fetch OHLC of the specific stock on the NSE within specified time-frame
- [ ] Make a csv and split into a 'test' and 'train' set
- [ ] Normalization
- [ ] LSTM Model
Long Short-Term Memory models are extremely powerful time-series models. They can predict an arbitrary number of steps into the future. An LSTM module (or cell) has 5 essential components which allows it to model both long-term and short-term data.

    - **Cell state (ct)** - This represents the internal memory of the cell which stores both short term memory and long-term memories
    - **Hidden state (ht)** - This is output state information calculated w.r.t. current input, previous hidden state and current cell input which you eventually use to predict the future stock market prices. Additionally, the hidden state can decide to only retrive the short or long-term or both types of memory stored in the cell state to make the next prediction.
    - **Input gate (it)** - Decides how much information from current input flows to the cell state
    - **Forget gate (ft)** - Decides how much information from the current input and the previous cell state flows into the current cell state
    - **Output gate (ot)** - Decides how much information from the current cell state flows into the hidden state, so that if needed LSTM can only pick the long-term memories or short-term memories and long-term memories
    - This is what the model looks like as a processing unit:
    ![](/src/lstm_model.jpg)

    - [ ] Data generator
    - [ ] Set inputs, outputs and hyperparameters
- [ ] Need a regression layer
- [ ] Feed LSTM ouput to regression 
- [ ] Loss calculation and Optimisation