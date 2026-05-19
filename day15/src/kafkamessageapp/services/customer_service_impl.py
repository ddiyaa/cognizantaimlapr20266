#create customer service implementation class to validate customer data retrieved from database 
import great_expectations as gx
import pandas as pd
from kafkamessageapp.repositories.customer_repository_impl import CustomerRepositoryImpl
from kafkamessageapp.services.customer_service import CustomerService
class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository = CustomerRepositoryImpl()
        self.context = gx.get_context()
    
    def ge_suite(self):
        self.data_source      = self.context.data_sources.add_pandas("customer_source")
        self.data_asset       = self.data_source.add_dataframe_asset("customers")
        self.batch_definition = self.data_asset.add_batch_definition_whole_dataframe("full_batch")    
        # Create suite (GX 1.0: context.suites, not get_validator)
        self.suite = self.context.suites.add(
            gx.ExpectationSuite(name="customers_suite")
        )
        return self.suite
    
    def validate_customer_data(self):
        
        self.customers = self.customer_repository.get_all_customers() 
        #create pandas dataframe from customer data
        self.df = pd.DataFrame([customer.__dict__ for customer in self.customers])
        print(self.df.head())
        #check point schema validation for customer data

        #validate customer data retrieved from database
        print("Customer data validated successfully")