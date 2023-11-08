from flask import jsonify

class MakeResponse:
    def __init__(self, name) -> None:
        self.name = name

    # 200 Success OK -> Used for returning objects
    def response_ok(self, data):
        '''
        Makes request for 200 OK response
        
        Parameters:
        - data (any) : The data fetched by the server
        '''
        return jsonify({
            "status" : "success",
            "data" : data
        }), 200

    # 201 CREATED -> send the id of the item created
    def created(self, message, data):
        '''
        Makes a 201 CREATED response. According to HTTP standard we must send the created id.
        
        Parameters:
        - message (string) : message on what or what type of object has been created.
        - data (any) : Id to access the element that has been just created. Using for testing purposes.
        '''
        return jsonify({
            "status" : "success",
            "message" : message,
            "data" : data
        }), 201
        
    # 204 NO Content -> Server has processed but nothing to send as response
    def no_content(self, data):
        '''
        Makes a NO CONTENT response. Server has processed it successfully but there is no data to send.
        
        Parameters:
        - data (any) : Item id that has been deleted
        '''
        return jsonify({
            "status" : "success",
            "message" : "Item has been deleted",
            "data" : data
        }), 204
        
        
    # 400 Bad request
    def bad_request(self, message, description):
        '''
        Makes a 400 BAD REQUEST response.
        
        Parameters:
        - message (string) : Indicate if the error is in database or request itself
        - description (any) : If database error add additional details such as err_no and err_mssg
        '''
        return jsonify({
            "status" : "error",
            "message" : message,
            "description" : description
        }), 400
        
    # 404 Data not found
    def data_not_found(self, message):
        '''
        Makes a 404 Data Not Found response.
        
        Parameters:
        - message (string) : Inform which field has no data.
        '''
        return jsonify({
            "status": "success",
            "message" : message,
            "data" : None
        }), 404
        
    
    # Database connection error
    def db_conn_error(self):
        '''
        Error related to Capstone project error. 
        Creates a Internal Server Error if database is not accessible.
        '''
        return jsonify({
            "status" : "error",
            "message" : "Database is not connected"
        }), 500
    
        
    # 503 Can't process request
    def service_unavailable(self, service_name):
        '''
        Makes a 503 SERVICE UNAVAILABLE response. Useful in microservices architecture.
        
        Parameters:
        - service_name (string) : service which is not available
        '''
        return jsonify({
            "status" : "error",
            "message" : f"{service_name} service is unavailable"
        }), 503
    