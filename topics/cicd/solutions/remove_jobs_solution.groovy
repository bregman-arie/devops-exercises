def jobs = Jenkins.instance.items.findAll { job -> job.name =~ /"test"/ }
    
jobs.each { job ->
    println job.name
    //job.delete()
}
