How my webmethods server works ?
My webMethods Server is a run-time container for functions made available by webMethods applications. The user interface in which you perform these functions is called My webMethods. My webMethods provides a ready-made environment in which users can perform functions on webMethods applications, and administrators can manage access to those functions. In addition, My webMethods Server gives you the capability to develop additional user interface pages, and a broad-based set of administrative tools with which to manage the increased capabilities.


JDBC Adapter details ?

Enable Connection Pooling	true

Minimum Pool Size 0 If connection pooling is enabled, this field specifies the number of connections to create when the connection is enabled. The adapter will keep open the number of connections you configure here regardless of whether these connections become idle.

Maximum Pool Size	150 If connection pooling is enabled, this field specifies the maximum number of connections that can exist at one time in the connection pool.

Pool Increment Size	2 If connection pooling is enabled, this field specifies the number of connections by which the pool will be incremented if connections are needed, up to the maximum pool size.

Block Timeout (msec)	1000 If connection pooling is enabled, this field specifies thenumber of milliseconds that Integration Server will wait to obtain a connection with the database before it times out and returns an error. For example, you have a pool with Maximum Pool Size of 20. If you receive 30 simultaneous requests for a connection, 10 requests willbe waiting for a connection from the pool. If you setthe Block Timeout to 5000, the 10 requests will wait for aconnection for 5 seconds before they time out and return an error. If the services using the connections require 10 seconds to complete and return connections to the pool, the pending requests will fail and return an error message stating that no connections are available. If you set the Block Timeout value too high, you may encounter problems during error conditions. If a request contains errors that delay the response, other requests will not be sent. This seeing should be tuned in conjunction with the Maximum Pool Size to accommodate such bursts in processing.

Expire Timeout (msec)	1000 If connection pooling is enabled, this field specifies the number of milliseconds that an inactive connection can remain in the pool before it is closed and removed from the pool. The connection pool will remove inactive connections until the number of connections in the pool is equal to the Minimum Pool Size. The inactivity timer for a connection is reset when the connection is used by the adapter. If you set the Expire Timeout value too high, you may have a number of unused inactive connections in the pool. This consumes local memory and a connection on your backend resource. This could have an adverse effect if your resource has a limited number of connections. If you set the Expire Timeout value too low, performance could degrade because of the increased activity of creating and closing connections. This setting should be tuned in conjunction with the Minimum Pool Size to avoid excessive opening/closing of connections during normal processing.

Startup Retry Count	0 The number of times that the system should attempt to initialize the connection pool at startup if the initial attempt fails. 

Startup Backoff Timeout (sec)	10 The number of seconds that the system should wait between attempts to initialize the connection pool.

Levels in logging ?
Off No messages.
Fatal Fatal messages only. This is the default
Error Error and fatal messages.
Warn Warning, error, and fatal messages.
Info Informational, warning, error, and fatal messages.
Debug Debug, informational, warning, error, and fatal messages.
Trace Trace, debug, informational, warning, error, and fatal messages.



UM clusters example ?
How do you send the acknowledgments in JMS ?
Triggers in clusters ?

Broker and UM differences ?
1. Supports many client APIs like Python, Javascript, iOS, Android, RESR and SOAP
2. Supports transport protocols HTTP, HTTPS, Multicast
3. Supports Group Based Permisssions
4. UI is MWS portlets, UI is Enterprise Manager
5. Supports Active-Active clustering
6. Message routing User subject based routing,Direct Delivery and Advanced selectors
7. Quality of service -- Transient(stores in memory only if there is active subscribers) and Simple (if message lost and sequncer number reset on restart)
8. Limit the capacity, Message reply
9. More than 100k concurrent connections and improve in performance

Publish and Subscriber ?
(IS) -- Publishing Service --> Dispatcher 
(Messaging Provider) -- Memory -- Guranteed Storage -- Queue or Channel
Document can be volatile or Guarnteed
Published and Delivered types -- Provider enqueues the document 
If time-to-live elapses broker discards the document
Broker uses Queue, UM uses Channel
If there is no subscribers -- Moves to dead letter queue

when Provider is unavailable
If the document is guaranteed and the client side queue is configured, the dispatcher routes the document to the client side queue.
If the document is guaranteed and the client side queue is not configured, Integration Server throws an ISRuntimeException.
If the document is volatile, the dispatcher discards the document and the publishing service throws an exception.

client side queue also called as outbound document store.


When the Drain CSQ in Order check box is selected, Integration Server continues to write new messages to the client side queue until the client side queue is completely drained.


Suscribing pattern
1. Integration Server retrieves documents for a webMethods messaging trigger from the webMethods messaging provider. Integration Server places the documents in the trigger’s queue.
2. Integration Server pulls a document from the trigger queue and evaluates the document against the conditions in the trigger.
3. If the document matches a trigger condition, Integration Server executes the trigger service associated with that condition.
If the document does not match a trigger condition, Integration Server discards the document and returns an acknowledgement to the webMethods messaging provider. Integration Server also generates a journal log message stating that the document did not match a condition.
4. 
a. If the trigger service executed successfully, Integration Server returns an acknowledgement to the webMethods messaging provider.
b. If a service exception occurs, the trigger service ends in error and Integration Server rejects the document. If the document is guaranteed, Integration Server returns an acknowledgement to the webMethods messaging provider. Integration Server sends an error document to indicate that an error has occurred.
c. If a transient error occurs during trigger service execution and the service catches the error, wraps it and re-throws it as an ISRuntimeException,
then Integration Server waits for the length of the retry interval and reexecutes the service using the original document as input. If Integration
Server reaches the maximum number of retries and the trigger service still fails because of a transient error, Integration Server treats the last failure as a service error.


A publishing service can deliver a document by specifying the destination of the document. That is, the publishing service specifies the Broker client that is to receive the document. When the Broker receives a delivered document, it places a copy of the document in the queue for the specified client only.


Local publishing refers to the process of publishing a document within the Integration Server. Only subscribers located on the same Integration Server can receive and process the document. In local publishing, the document remains within Integration Server. There is no involvement with the webMethods messaging provider.

An instance of a publishable document type is published locally in the following
situations:
i. When the Broker connection alias is assigned to the publishable document type and the service that publishes the document specifies that the document should be published locally.
ii. When the default messaging connection alias is assigned to the publishable document type and the default messaging connection alias is set to
IS_LOCAL_CONNECTION.


pub.publish:deliver Delivers a document to a specified destination.
pub.publish:deliverAndWait Delivers a document to a specified destination and waits for a response.
pub.publish:publish Publishes a document locally or to a configured messaging provider (Universal Messaging or Broker). Any clients (triggers) with 
			subscriptions to documents of this type will receive the document.
pub.publish:publishAndWait Publishes a document locally or to a configured messaging provider (Universal Messaging or Broker) and waits for a
			response. Any clients (triggers) with subscriptions for the published document will receive the document.
pub.publish:reply Delivers a reply document in answer to a document received by the client.
pub.publish:waitForReply Retrieves the reply document for a request published asynchronously.



An activation ID is a unique identifier assigned to a published document. Subscribing triggers use the activation ID to determine whether a document satisfies a join condition. Integration Server stores the activation ID in the activation field of a document envelope. By default, Integration Server assigns the same activation ID to each document published within a single top-level service. For example, suppose the processPO service publishes a newCustomer document, a checkInventory document, and a confirmOrder document. Because all three documents are published within the processPO service,
Integration Server assigns all three documents the same activation ID.


A refill level can be set for webMethods messaging triggers that receive documents from the webMethods Broker only. Refill level does not apply
to webMethods messaging triggers that receive documents from Universal Messaging.

Integration Server returns acknowledgements for guaranteed documents only. Integration Server does not return acknowledgements for volatile documents.

You specifically resume document retrieval or document processing for the webMethods messaging trigger. You can resume document retrieval and document processing using Integration Server Administrator, built-in services (pub.trigger:resumeProcessing or pub.trigger:resumeRetrieval), or by calling methods in the Java API (com.wm.app.b2b.server.dispatcher.trigger.TriggerFacade.setProcessingSuspended() and com.wm.app.b2b.server.dispatcher.trigger.TriggerFacade.setRetrievalSuspended()).

Integration Server restarts, the webMethods messaging trigger is enabled or disabled (and then re-enabled), the package containing the webMethods messaging trigger reloads. (When Integration Server suspends document retrieval and document processing for a webMethods messaging trigger because of an error, Integration Server considers the change to be temporary.)

If the trigger service is a flow service, the trigger service must invoke pub.flow:throwExceptionForRetry

A resource monitoring service must do the following:
Use the pub.trigger:resourceMonitoringSpec as the service signature.
Check the availability of the resources used by the document resolver service and all the trigger services associated with a trigger. Keep in mind that each condition in a trigger can be associated with a different trigger service. However, you can only
specify one resource monitoring service per trigger.
Return a value of “true” or “false” for the isAvailable output parameter. The author
of the resource monitoring service determines what criteria makes a resource
available.
Catch and handle any exceptions that might occur. If the resource monitoring service
ends because of an exception, Integration Server logs the exception and continues
as if the resource


In addition to the data contained in the SOAP body, a SOAP message might contain
data in the SOAP headers. The best way to access the SOAP headers is to use handlers.
A handler, sometimes called a header handler, provides access to the entire SOAP
message.
Handlers can be used to perform various types of processing, including processing
SOAP headers, adding SOAP headers, removing SOAP headers, passing data from
the header to the endpoint service or vice versa. Provider and consumer web service
descriptors can use handlers.
In Integration Server, a handler is a set of up to three handler services. The handler can
contain one of each of the following handler services:
Request handler service
Response handler service
Fault handler service


A binder is a webMethods term for a collection of related definitions and specifications
for a particular port. The binder is a container for the endpoint address, WSDL binding
element, transport protocol, and communication protocol information. Designer creates
at least one binder when it generates the web service descriptor based on the data in
the WSDL or IS service






















