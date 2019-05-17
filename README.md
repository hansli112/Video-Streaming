# Video-Streaming
Intro to Computer Network term project


## What is Video-Streaming?
Streaming media is multimedia that is constantly received by and presented to an end-user while being delivered by a provider. The verb "to stream" refers to the process of delivering or obtaining media in this manner; the term refers to the delivery method of the medium, rather than the medium itself, and is an alternative to file downloading, a process in which the end-user obtains the entire file for the content before watching or listening to it.


## Goal
- It must to transmit video as video-streaming way , and successfully play on the client side.


## Implementation
- Basic

	- Video is transferred to the server , and the server transfers video to other clients
		- Client upload video to server
		- The server sends the video to the watching client.
			- Flask: A micro web framework written in Python. 
				- Aoubt Flask
					- It is classified as a microframework because it does not require particular tools or libraries.It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 
					- Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.
				- Step
					- Flask provides native support for streaming responses by using generator functions.
					- The generator is a special function that can be interrupted and restored.
					- Video streaming can generate large data tables without having to put the entire table in memory

- Functions(about Network)

	- Security
		- AES Encryption (choose one of modes: ECB, CBC, OFB, CFB, CTR, XTS)

- Other Functions

	- Message system
		- Allow users instantly to upload ideas and thoughts about the vedio.
		- Use the send and recv functions in the socket to achieve.
