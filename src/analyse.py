def analyse_users(df):
    
    new_dict = {'total_users': len(df),
                'gender_count':df['gender'].value_counts().to_dict(),
                'top_five_countries': df['country'].value_counts().head(5).to_dict(),
                'duplicate_count': int(df.duplicated().sum()),
                'null_count': df.isnull().sum().to_dict()
                }
    return new_dict

    