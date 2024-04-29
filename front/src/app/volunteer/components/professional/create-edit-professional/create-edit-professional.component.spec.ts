import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditProfessionalComponent } from './create-edit-professional.component';

describe('CreateEditProfessionalComponent', () => {
  let component: CreateEditProfessionalComponent;
  let fixture: ComponentFixture<CreateEditProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
