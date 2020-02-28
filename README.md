# container-commit
Experiment with docker commit using a simple python file

Steps
 1. Run ``docker-compose up -d``
 2. Run ``docker images | grep test``. You will see an image named ``test`` with tag as ``latest``
 3. Run ``docker ps`` to find the container id of the running container 
 4. Run ``docker commit <<container_id>> test:v2``. This would create another image test:v2.
     Verify this by running ``docker images | grep test``
 5. Run ``docker-compose down`` to stop the container spawned using image ``test:latest``
 6. Check the numver in myfile using ``cat myfile``. Note the number.
 7. Delete this file now ``rm myfile``
 8. Start a new container from the new image ``test:v2``. Run ``docker-compose -f docker-compose-v2.yaml up -d`` 
 9. Repeat step 6 and you will observe that the number is jut more than what we saw in step 6

The program starts from 0 and after every 5 seconds write to 2 files - one inside docker and another in the mapped volume. It writes the same number to both the files. Before writing it tries to read the file that is only inside the container. If the file does not exist, it reads as 0 and starts incrementing from there.

When we start using the second image, we observe that it starts from where the first container left. This shows that [docker's commit](https://docs.docker.com/engine/reference/commandline/commit/) command does infact work.  

