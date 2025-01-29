# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. Connect to serverless compute. Run through the cells
# MAGIC 3. Run the cells for deploying and running the dev job

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Workflows
# MAGIC
# MAGIC Workflows is on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A job explains the tasks to be run and the conditions that need to be met (e.g. wait for task X to succeed first). A job run is an execution of the job and performs the task as specified in the job.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Write answer in the empty cell below.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC An example name is `acme_transport_taxinyc_prep_dev_jonas_featgh10620127001_4c6799ab`. The name follows the folder structure of the code and gives a clear idea which job has been run.
