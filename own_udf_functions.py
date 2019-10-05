#### Show index and respective column name for a dataset ####

def show_description(dataset):
    
    for i in range (1,len(dataset.columns)+1):
        description = str(i-1) + ': ' + dataset.columns[i-1]
        print(description)
        
#### Optimized version of GridSearch Algorithm ####
        
        
def opt_grid_search(object_name, params_set, cross_val = 2, def_params = None):

    exec_string = 'opt_object = ' + object_name + '(' + def_params + ')'
        
    print(exec_string)
    
    dict_keys = list(params_set[0].keys())
    dict_values = list(params_set[0].values())
    
    #### Start of the loop ####
    
    estimations = [] ## Rates for all of the possible models
    total_time = 0 
    
    exec(exec_string) 
    opt_object.fit(X_train,y_train) 
    
    accuracies = cross_val_score(estimator = opt_object, X = X_test, y = y_test, cv = cross_val, n_jobs = -1) 
    estimations.append('Iteration ' + str(1) + ' ||| ' + ' mean: ' + str(round(accuracies.mean(),4)) + ' std: ' + str(round(accuracies.std(),4)))
    
    #### Final loop ####
    
    for i in range(1,len(params_set[1])):  
        
        parameters_set = {}
        
        parameters = dict_keys[i]
        values = dict_values[i]
    
        parameters_set[parameters] = values
        print(parameters_set)  
    
    #### Count execution time ####
    
        import time
        start = time.time()
        
    #### Execute Grid Search Alghorithm ####
        
        grid_search = GridSearchCV(estimator = opt_object, 
                                   param_grid = parameters_set,
                                   cv = cross_val,
                                   n_jobs = -1)
    
        grid_search = grid_search.fit(X_train, y_train) 
    
    #### Koniec pomiaru czasu #####
        
        end = time.time()
        exec_time = end-start
        total_time = total_time + exec_time 
        
        best_accuracy = grid_search.best_score_
        best_parameters = grid_search.best_params_
        
    #### Read best parameters ####
    
        for key, value in best_parameters.items():
            new_parameter = str(key) + '=' + str(value)
        
    #### Regressor update ####
            
        exec_string = exec_string.replace(')',',') + str(new_parameter) + ')'
        print(exec_string)
        exec(exec_string) 
        opt_object.fit(X_train,y_train) 
        
    #### Model k-fold Cross Validation + zrzut wynikow ####
        print('Optimized object:' + str(opt_object))
        accuracies = cross_val_score(estimator = opt_object, X = X_test, y = y_test, cv = cross_val, n_jobs = -1)
        estimations.append('Iteration ' + str(i+1) + ' ||| ' + ' mean: ' + str(round(accuracies.mean(),4)) + ' std: ' + str(round(accuracies.std(),4)))
        
        print(accuracies)        
        print(total_time)
        
#### Example call of OGS function ####
        
""" 
object_name = 'SVR'
def_params = 'kernel = \'rbf\''
cross_val = 2
params_set = [
              {'kernel': ['rbf', 'poly','sigmoid'],
               'gamma' : np.arange(0.0, 1.0, 0.1),
               'C': np.arange(1, 10, 1), 
               'epsilon': np.arange(0.0, 1.0, 0.1),
               'coef0': np.arange(0.0, 1.0, 0.1)}]
    
opt_grid_search(object_name, params_set, cross_val = 2, def_params = def_params)
"""