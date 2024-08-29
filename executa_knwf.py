
#importar biblioteca knime Baixe ela antes de executar esse scripit#
import knime


# In[2]:


#Caminho até o executavel do Knime#
knime.executable_path = "C:\\knime 5.1.0\\"


#caminho até o WorkSpace#
workspace ="C:\\Users\\seu user\\knime-workspace"

#Nome Do WorkFlow#
workflow_deployment ="\\seu wk"


knime.Workflow(workflow_path=workflow_deployment,workspace_path=workspace)


# In[3]:


#condição de execução do workflow#
with knime.Workflow(workflow_path=workflow_deployment,workspace_path=workspace) as wf:
    #executar#
    wf.execute()


# In[4]:


#mensagem pós execução#
print("finalizado")
