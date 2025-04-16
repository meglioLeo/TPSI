git config --global --unset user.name
git config --global --unset user.email
echo "Configurazioni Git rimosse."

if [[ "$1" == "--set" ]]; then
    git config --global user.name "meglioLeo"
    git config --global user.email "leonardo.cresti@students.sarrocchi.it"
    echo "Configurazioni Git aggiornate."