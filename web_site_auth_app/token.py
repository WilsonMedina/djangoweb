from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.utils import six  

#---------------------Generator of token for confirmation of register and reset password--------------------#
class TokenGenerator(PasswordResetTokenGenerator):  

    def make_hash_value(self, user, timestamp):  
        return (  
            six.text_type(user.pk) + six.text_type(timestamp) +  
            six.text_type(user.is_active)  
        )  
account_activation_token = TokenGenerator()  