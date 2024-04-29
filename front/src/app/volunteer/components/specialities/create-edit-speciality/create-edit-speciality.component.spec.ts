import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditSpecialityComponent } from './create-edit-speciality.component';

describe('CreateEditSpecialityComponent', () => {
  let component: CreateEditSpecialityComponent;
  let fixture: ComponentFixture<CreateEditSpecialityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditSpecialityComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditSpecialityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
