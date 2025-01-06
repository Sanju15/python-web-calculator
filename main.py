from flask import Flask, render_template, request #,flash
import re

app = Flask(__name__, 
            template_folder='src/templates')
            
# app.secret_key = 'your-secret-key-here'  # Required for flash messages

def is_valid_number(number_str):
    """Validate if the input string is a valid number."""
    # Check if empty
    if not number_str:
        return False
    
    pattern = r'^\-?\d*\.?\d+$'# Regular expression for valid number format (integers and decimals)
    return bool(re.match(pattern, number_str))

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        num1_str = request.form.get('num1', '').strip()
        num2_str = request.form.get('num2', '').strip()
        operation = request.form.get('operation')
        
        # Validate inputs
        if not is_valid_number(num1_str):
            error = "First number is invalid. Please enter a valid number."
        elif not is_valid_number(num2_str):
            error = "Second number is invalid. Please enter a valid number."
        else:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                
                # calculation
                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    if num2 == 0:
                        error = "Error: Cannot divide by zero"
                    else:
                        result = num1 / num2
                
                # Remove trailing zeros after decimal
                if result is not None:
                    if result.is_integer():
                        result = int(result)
                    else:
                        # Limit to decimal places
                        result = "{:.4f}".format(result).rstrip('0').rstrip('.')
                        
            except ValueError:
                error = "Invalid number format. Please check your inputs."
            except Exception as e:
                error = f"An error occurred: {str(e)}"
    
    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)