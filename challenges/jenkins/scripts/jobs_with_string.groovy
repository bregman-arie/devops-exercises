def jobs = Jenkins.instance.items.findAll { job -> job.name =~ /"REMOVE_ME"/ }
    
jobs.each { job ->
    println job.name
    //job.delete()
}
