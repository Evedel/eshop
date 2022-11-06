# Motivation
The original [flant/shell-operator](https://github.com/flant/shell-operator) is pretty good.  
Very configurable and flexible, forget about operator lifecycle and concentrate on business logic.  
But, what if your code is already well organised.  
You don't need to leak complex logic outside to decide which object to process.  
You don't want to repeat having all the same hooks configuration for many crds.  
Well, this is the answer: use flant operator with this wrapper.

1. Write you operator business logic so it is reentrant and idempotent  
    (so now you have an entrypoint you can run manually and debug)  
    (something like [on_secrets_events entrypoint](./app/v1/bin/on_secrets_events))
2. Call the processing of each crd/object in the same way  
    (something like `./app/v1/bin/on_secrets_events namesapce object`)
3. The configuration of flant-operator can be then extremely simplified and unified  
    (something lie [on_secrets_events hook](./app/hooks/bin/on_secrets_events))

# To setup in vscode:

1. copy example setup
    ```
    cp -r example.devcontainer .devcontainer
    ```
2. reopen in devcontainer

# To run tests manually

1. Out of the devcontainer:
    ```
    ./bin/test
    ```
2. In devcontainer:  
    Should be autodiscoverable


# To run operator manually
Open devcontainer's cli (`` ctrl+` ``), and run
```
/shell-operator
```
If you don't have a long lived cluster, you can use kind setup:
1. as it is going to be dind setup, we need to bind lical kubernetes to host ip
    ```
    ifconfig eth0 | awk '/inet / {print $2; }' | cut -d ' ' -f 2
    ```
2. plug the output into `apiServerAddress` in `./kind/config.yaml`
3. create cluster
    ```
    kind create cluster --config config.yaml
    ```
4. run the operator in vscode cli
    ```
    /shell-operator
    ```