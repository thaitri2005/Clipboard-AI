# Configuration file for Local AI Clipboard
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# OLLAMA CONFIGURATION (Ctrl+Shift+G)
# ============================================================

# Ollama model to use
# Recommended lightweight models for SQL:
# - "sqlcoder:7b" - Specialized for SQL (7GB)
# - "codellama:7b" - Good for code including SQL (3.8GB) 
# - "phi3:mini" - Very lightweight, handles SQL well (2.3GB) ⭐ RECOMMENDED
# - "qwen2.5-coder:1.5b" - Smallest, fast, decent SQL (1GB)
MODEL = "phi3:mini"

# Optional: Add a system prompt to customize AI behavior
# Leave empty for default behavior
# For SQL tasks, you might want:
# - "You are an SQL expert. Help with the following SQL query:"
# - "Explain this SQL query in simple terms:"
# - "Optimize the following SQL query:"
# - "Convert this to SQL:"
SYSTEM_PROMPT = '''
You are an expert SQL assistant. I am preparing for my SQL midterm. Below is my full database schema. Please load it into your context and wait. In the next message, I will ask SQL questions and you must answer using correct SQL queries based on this schema.

Database Schema:

customers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
employee privileges: [Employee ID, Privilege ID]
employees: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
inventory transaction types: [ID, Type Name]
inventory transactions: [Transaction ID, Transaction Type, Transaction Created Date, Transaction Modified Date, Product ID, Quantity, Purchase Order ID, Customer Order ID, Comments]
invoices: [Invoice ID, Order ID, Invoice Date, Due Date, Tax, Shipping, Amount Due]
order details: [ID, Order ID, Product ID, Quantity, Unit Price, Discount, Status ID, Date Allocated, Purchase Order ID, Inventory ID]
order details status: [Status ID, Status Name]
orders: [Order ID, Employee ID, Customer ID, Order Date, Shipped Date, Shipper ID, Ship Name, Ship Address, Ship City, Ship State/Province, Ship ZIP/Postal Code, Ship Country/Region, Shipping Fee, Taxes, Payment Type, Paid Date, Notes, Tax Rate, Tax Status, Status ID]
orders status: [Status ID, Status Name]
orders tax status: [ID, Tax Status Name]
privileges: [Privilege ID, Privilege Name]
products: [Supplier IDs, ID, Product Code, Product Name, Description, Standard Cost, List Price, Reorder Level, Target Level, Quantity Per Unit, Discontinued, Minimum Reorder Quantity, Category, Attachments]
purchase order details: [ID, Purchase Order ID, Product ID, Quantity, Unit Cost, Date Received, Posted To Inventory, Inventory ID]
purchase order status: [Status ID, Status]
purchase orders: [Purchase Order ID, Supplier ID, Created By, Submitted Date, Creation Date, Status ID, Expected Date, Shipping Fee, Taxes, Payment Date, Payment Amount, Payment Method, Notes, Approved By, Approved Date, Submitted By]
sales reports: [Group By, Display, Title, Filter Row Source, Default]
shippers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
strings: [String ID, String Data]
suppliers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]

'''

# Timeout for Ollama response (seconds)
# Increase this if you get timeout errors
# First run might be slow as model loads into memory
TIMEOUT = 300  # 5 minutes (increased from 120s)

# ============================================================
# GEMINI API CONFIGURATION (Ctrl+Shift+H)
# ============================================================

# Get your API key from: https://makersuite.google.com/app/apikey
# Set this in your .env file: GEMINI_API_KEY=your-key-here
# The .env file is gitignored for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Gemini model to use
# Available models:
# - "gemini-2.0-flash-exp" - Latest and fastest ⭐ RECOMMENDED
# - "gemini-1.5-flash" - Fast and efficient
# - "gemini-1.5-pro" - More capable, slower
GEMINI_MODEL = "gemini-2.5-pro"

# Optional: System prompt for Gemini (can be different from Ollama)
# Leave empty to use the same SYSTEM_PROMPT as Ollama
GEMINI_SYSTEM_PROMPT = '''
You are an expert SQL assistant. I am preparing for my SQL midterm. Below is my full database schema. Please load it into your context and wait. In the next message, I will ask SQL questions and you must answer using correct SQL queries based on this schema.

Database Schema:

customers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
employee privileges: [Employee ID, Privilege ID]
employees: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
inventory transaction types: [ID, Type Name]
inventory transactions: [Transaction ID, Transaction Type, Transaction Created Date, Transaction Modified Date, Product ID, Quantity, Purchase Order ID, Customer Order ID, Comments]
invoices: [Invoice ID, Order ID, Invoice Date, Due Date, Tax, Shipping, Amount Due]
order details: [ID, Order ID, Product ID, Quantity, Unit Price, Discount, Status ID, Date Allocated, Purchase Order ID, Inventory ID]
order details status: [Status ID, Status Name]
orders: [Order ID, Employee ID, Customer ID, Order Date, Shipped Date, Shipper ID, Ship Name, Ship Address, Ship City, Ship State/Province, Ship ZIP/Postal Code, Ship Country/Region, Shipping Fee, Taxes, Payment Type, Paid Date, Notes, Tax Rate, Tax Status, Status ID]
orders status: [Status ID, Status Name]
orders tax status: [ID, Tax Status Name]
privileges: [Privilege ID, Privilege Name]
products: [Supplier IDs, ID, Product Code, Product Name, Description, Standard Cost, List Price, Reorder Level, Target Level, Quantity Per Unit, Discontinued, Minimum Reorder Quantity, Category, Attachments]
purchase order details: [ID, Purchase Order ID, Product ID, Quantity, Unit Cost, Date Received, Posted To Inventory, Inventory ID]
purchase order status: [Status ID, Status]
purchase orders: [Purchase Order ID, Supplier ID, Created By, Submitted Date, Creation Date, Status ID, Expected Date, Shipping Fee, Taxes, Payment Date, Payment Amount, Payment Method, Notes, Approved By, Approved Date, Submitted By]
sales reports: [Group By, Display, Title, Filter Row Source, Default]
shippers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]
strings: [String ID, String Data]
suppliers: [ID, Company, Last Name, First Name, E-mail Address, Job Title, Business Phone, Home Phone, Mobile Phone, Fax Number, Address, City, State/Province, ZIP/Postal Code, Country/Region, Web Page, Notes, Attachments]

'''

# ============================================================
# GENERAL SETTINGS
# ============================================================

# Show verbose output in terminal
VERBOSE = True
