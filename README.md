# Fourier Transform Demo

An interactive Python program that demonstrates the Fourier Transform using ASCII terminal graphs.

## Features

- Generate three waveform types: sine, square, and sawtooth
- Display time domain waveforms as ASCII art
- Compute and display the frequency domain (FFT magnitude spectrum)
- Interactive menu for selecting waveforms

## Usage

Install dependencies:

```
pip install -r requirements.txt
```

Run the program:

```
python fourier_demo.py
```

Select a waveform from the menu and the program will display both the time domain and frequency domain graphs in your terminal.

## Sample Output

### Sine Wave

```
  === Time Domain - Sine Wave ===

   1.00 |    **                *                **                *
        |   *  *              * **             *  *              * **
        |       *            *                     *            *
        |  *                      *           *                      *
        |        *          *                       *          *
        |
        | *                        *         *                        *
   0.00 |*        *        *                *        *        *
        |                 *         *                        *         *
        |
        |          *                       *          *                       *
        |                *           *                      *           *
        |           *                     *            *                     *
        |            *  *             ** *              *  *             ** *
  -1.00 |             **                *                **                *
        +----------------------------------------------------------------------

  === Frequency Domain - Sine Wave (magnitude) ===

   1.00 |         **
        |
        |
        |
        |
        |
        |
   0.50 |
        |
        |
        |
        |
        |
        |
   0.00 |*********  ***********************************************************
        +----------------------------------------------------------------------
```

### Square Wave

```
  === Time Domain - Square Wave ===

   1.00 |*********         *********        *********         *********
        |
        |
        |
        |
        |
        |
   0.00 |
        |
        |
        |
        |
        |
        |
  -1.00 |         *********         ********         *********         ********
        +----------------------------------------------------------------------

  === Frequency Domain - Square Wave (magnitude) ===

   1.28 |         **
        |
        |
        |
        |
        |
        |
   0.64 |
        |
        |                           **
        |
        |                                            **
        |                                                              **
        |
   0.00 |*********  ****************  ***************  ****************  ******
        +----------------------------------------------------------------------
```

### Sawtooth Wave

```
  === Time Domain - Sawtooth Wave ===

   0.94 |                 *                *                 *                *
        |                *                *                 *                *
        |               *                *                 *                *
        |              *                *                 *                *
        |             *                *                 *                *
        |           **               **                **               **
        |          *                *                 *                *
  -0.03 |         *                *                 *                *
        |        *                *                 *                *
        |      **               **                **               **
        |     *                *                 *                *
        |    *                *                 *                *
        |   *                *                 *                *
        |  *                *                 *                *
  -1.00 |**                *                **                *
        +----------------------------------------------------------------------

  === Frequency Domain - Sawtooth Wave (magnitude) ===

   0.64 |         **
        |
        |
        |
        |
        |
        |
   0.32 |                  **
        |
        |                           **
        |                                   ***
        |                                            **
        |                                                     **       **
        |***
   0.00 |   ******  *******  *******  ******   ******  *******  *******  ******
        +----------------------------------------------------------------------
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
