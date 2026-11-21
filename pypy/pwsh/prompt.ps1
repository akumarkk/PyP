function prompt {
    $Branch = git rev-parse --abbrev-ref HEAD 2>$null
    if ($Branch) {
        "$($PWD.Path) ($Branch)> "
    }
    else {
        "$($PWD.Path)> "
    }
}

Add-Content -Path $PROFILE -Value @'
function prompt {
    "PS $($PWD.Path)> "
}
'@