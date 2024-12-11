# delete from public.mc_files 
# 
# select * from public.mc_files 
# 
# CREATE TABLE public.mc_files (
#     id SERIAL PRIMARY KEY,                  -- Auto-generated id
#     org_id INTEGER ,                -- Organization ID
#     processed_files VARCHAR,                -- Processed files, could be an array or simple text
#     created_date TIMESTAMP DEFAULT NOW()    -- Timestamp for creation, default is current timestamp
# );